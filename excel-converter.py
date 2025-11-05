#!/usr/bin/env python3

import pandas as pd
import json
from datetime import datetime
import argparse
import re
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

class ExcelConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel to JSON Converter")
        
        # Set minimum window size
        self.root.minsize(500, 200)
        
        # Configure grid weight
        self.root.grid_columnconfigure(1, weight=1)
        
        # Create main frame with padding
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.grid_columnconfigure(1, weight=1)
        
        # Excel file selection
        ttk.Label(main_frame, text="Excel File:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.excel_path = tk.StringVar()
        self.excel_entry = ttk.Entry(main_frame, textvariable=self.excel_path)
        self.excel_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_excel).grid(row=0, column=2)
        
        # JSON save location
        ttk.Label(main_frame, text="Save JSON to:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.json_path = tk.StringVar()
        self.json_entry = ttk.Entry(main_frame, textvariable=self.json_path)
        self.json_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_json).grid(row=1, column=2)
        
        # Convert button
        self.convert_btn = ttk.Button(main_frame, text="Convert", command=self.convert)
        self.convert_btn.grid(row=2, column=0, columnspan=3, pady=20)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        # Status label
        self.status_var = tk.StringVar()
        self.status_label = ttk.Label(main_frame, textvariable=self.status_var)
        self.status_label.grid(row=4, column=0, columnspan=3, pady=5)
        
        # Initialize paths
        self.last_directory = os.path.expanduser("~")
        
    def browse_excel(self):
        filename = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=[("Excel files", "*.xlsx *.xls"), ("All files", "*.*")],
            initialdir=self.last_directory
        )
        if filename:
            self.last_directory = os.path.dirname(filename)
            self.excel_path.set(filename)
            # Auto-generate JSON path
            json_path = os.path.splitext(filename)[0] + '.json'
            self.json_path.set(json_path)
    
    def browse_json(self):
        initial_file = ''
        initial_dir = self.last_directory
        
        # If Excel path is set, use its directory and name for the JSON
        if self.excel_path.get():
            excel_path = self.excel_path.get()
            initial_dir = os.path.dirname(excel_path)
            initial_file = os.path.splitext(os.path.basename(excel_path))[0] + '.json'
        
        filename = filedialog.asksaveasfilename(
            title="Save JSON As",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            initialdir=initial_dir,
            initialfile=initial_file
        )
        if filename:
            self.last_directory = os.path.dirname(filename)
            # Ensure the filename ends with .json
            if not filename.lower().endswith('.json'):
                filename += '.json'
            self.json_path.set(filename)
    
    def convert(self):
        excel_file = self.excel_path.get()
        json_file = self.json_path.get()
        
        if not excel_file or not json_file:
            messagebox.showerror("Error", "Please select both input and output files.")
            return
            
        # Ensure Excel file exists
        if not os.path.exists(excel_file):
            messagebox.showerror("Error", f"Excel file not found: {excel_file}")
            return
            
        # Ensure JSON path is valid
        try:
            json_dir = os.path.dirname(json_file)
            if json_dir and not os.path.exists(json_dir):
                os.makedirs(json_dir)
        except Exception as e:
            messagebox.showerror("Error", f"Cannot create directory for JSON file: {str(e)}")
            return
        
        self.progress.start()
        self.status_var.set("Converting...")
        self.convert_btn.state(['disabled'])
        
        try:
            convert_excel_to_json(excel_file, json_file)
            self.status_var.set("Conversion successful!")
            messagebox.showinfo("Success", f"Successfully converted to {json_file}")
        except Exception as e:
            self.status_var.set("Error during conversion")
            messagebox.showerror("Error", f"Conversion error: {str(e)}")
        finally:
            self.progress.stop()
            self.convert_btn.state(['!disabled'])

def run_gui():
    root = tk.Tk()
    app = ExcelConverterGUI(root)
    root.mainloop()

def clean_lot_number(val):
    """Keep lot numbers as strings, just clean up whitespace"""
    if pd.isna(val):
        return None
    # Convert to string and clean up whitespace
    return str(val).strip()

def parse_provenance(text):
    """Convert bullet-pointed text into an array of strings"""
    if pd.isna(text):
        return []
    
    # Convert to string and handle line breaks
    text = str(text).replace('\r\n', '\n').replace('\r', '\n')
    
    # Split into lines and clean up
    lines = text.split('\n')
    items = []
    
    for line in lines:
        # Remove common bullet points and leading/trailing whitespace
        line = re.sub(r'^[\s•\-\*]+', '', line)  # Remove leading bullets
        line = re.sub(r'^\d+\.?\s*', '', line)   # Remove leading numbers
        line = line.strip()
        
        if line:  # Only add non-empty lines
            items.append(line)
    
    # Remove duplicates while preserving order
    seen = set()
    items = [x for x in items if not (x in seen or seen.add(x))]
    
    return items

def format_date(date_str):
    """Format date string to ISO format"""
    if pd.isna(date_str):
        return None
    
    try:
        # Handle various date formats
        if isinstance(date_str, (int, float)):
            # Handle Excel serial dates
            date_obj = pd.Timestamp('1899-12-30') + pd.Timedelta(days=int(date_str))
        else:
            # Try parsing as datetime with various formats
            date_obj = pd.to_datetime(date_str, dayfirst=False, yearfirst=False)
        
        # Always return in ISO format with time component
        return date_obj.strftime('%Y-%m-%dT%H:%M:%S')
    except:
        return None

def convert_excel_to_json(excel_file, output_file):
    """Convert Excel file to JSON format for the Sawhill tracking table"""
    
    # Read Excel file with string type for lot number column
    df = pd.read_excel(
        excel_file,
        dtype={'1979 Sawhill Lot Number': str, 'Sawhill Lot': str, 'Lot': str}
    )
    
    # Print the column types to debug
    print("\nDataFrame column types:")
    print(df.dtypes)
    
    # Always include these fields in the output JSON
    required_fields = [
        '1979 Sawhill Lot Number',
        '1979 Sawhill Description',
        'MHS Auction Lot Number',
        'Date Recorded',
        'Provenance',
        'Persistent URL'
    ]
    
    # Map Excel column names to JSON field names (case-insensitive)
    column_mapping = {
        # Very specific matches first
        '1979 sawhill lot number': '1979 Sawhill Lot Number',
        'sawhill lot number': '1979 Sawhill Lot Number',
        'sawhill lot': '1979 Sawhill Lot Number',
        '1979 lot': '1979 Sawhill Lot Number',
        '1979 lot number': '1979 Sawhill Lot Number',
        
        # MHS specific matches
        'mhs auction lot number': 'MHS Auction Lot Number',
        'mhs lot number': 'MHS Auction Lot Number',
        'mhs lot': 'MHS Auction Lot Number',
        'mhs number': 'MHS Auction Lot Number',
        'mhs': 'MHS Auction Lot Number',
        
        # Other fields
        'sawhill description': '1979 Sawhill Description',
        '1979 sawhill description': '1979 Sawhill Description',
        'description': '1979 Sawhill Description',
        
        'date recorded': 'Date Recorded',
        'date found': 'Date Recorded',
        'date': 'Date Recorded',
        
        'provenance': 'Provenance',
        'history': 'Provenance',
        
        'persistent url': 'Persistent URL',
        'url': 'Persistent URL',
        'link': 'Persistent URL'
    }
    
    # Print available columns in Excel file
    print("\nAvailable columns in Excel file:")
    for col in df.columns:
        print(f"  {col}")
    
    # Try to map Excel columns to JSON fields
    excel_to_json_mapping = {}
    for excel_col in df.columns:
        # Try exact match first (case-insensitive)
        key = excel_col.lower().strip()
        if key in column_mapping:
            excel_to_json_mapping[excel_col] = column_mapping[key]
            continue
            
        # If no exact match, look for specific patterns
        if 'sawhill' in key and ('lot' in key or 'number' in key) and 'mhs' not in key:
            excel_to_json_mapping[excel_col] = '1979 Sawhill Lot Number'
        elif 'mhs' in key and ('lot' in key or 'number' in key):
            excel_to_json_mapping[excel_col] = 'MHS Auction Lot Number'
        else:
            # For other fields, try partial matches but be more careful
            for possible_name, json_field in column_mapping.items():
                if (possible_name in key or key in possible_name) and not (
                    # Avoid confusing lot number fields
                    ('mhs' in key and json_field == '1979 Sawhill Lot Number') or
                    ('sawhill' in key and json_field == 'MHS Auction Lot Number')
                ):
                    excel_to_json_mapping[excel_col] = json_field
                    break
    
    print("Detected column mappings:")
    for excel_col, json_field in excel_to_json_mapping.items():
        print(f"  {excel_col} -> {json_field}")
    
    # Create new dataframe with mapped columns
    json_data = []
    
    for _, row in df.iterrows():
        entry = {field: None for field in required_fields}  # Initialize all fields as null
        
        # Map each column to its JSON equivalent
        for excel_col, json_col in excel_to_json_mapping.items():
            value = row[excel_col]
            
            # Apply specific formatting based on column
            if pd.isna(value):
                value = None
            elif json_col == '1979 Sawhill Lot Number':
                # Ensure we keep the original string value
                value = str(value).strip()
            elif json_col == 'Provenance':
                value = parse_provenance(value)
            elif json_col == 'Date Recorded':
                value = format_date(value)
            elif json_col == '1979 Sawhill Description':
                value = str(value).strip()
            elif json_col == 'Persistent URL':
                value = str(value).strip()
            
            # Add some debug printing
            if json_col == '1979 Sawhill Lot Number':
                print(f"Processing lot number: raw={row[excel_col]}, type={type(row[excel_col])}, final={value}")
            
            entry[json_col] = value
        
        json_data.append(entry)
    
    # Write to JSON file with proper formatting
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully converted {excel_file} to {output_file}")
    print(f"Processed {len(json_data)} entries")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Excel file to Sawhill tracking JSON format')
    parser.add_argument('--gui', action='store_true', help='Launch the GUI interface')
    parser.add_argument('--excel_file', help='Path to the input Excel file')
    parser.add_argument('--output_file', help='Path to the output JSON file')
    
    args = parser.parse_args()
    
    if args.gui or (not args.excel_file and not args.output_file):
        run_gui()
    elif args.excel_file and args.output_file:
        convert_excel_to_json(args.excel_file, args.output_file)
    else:
        parser.print_help()