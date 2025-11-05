---
layout: page
title: Tracking Sawhill
description: Following Sawhill's coins from 1979 to the present
img: assets/img/tracking_project/colosseum-sestertius-sawhill.jpg
importance: 4
category: work
pretty_table: true
---
<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/tracking_project/colosseum-sestertius-cng-record.jpg" class="img-fluid rounded z-depth-1"  zoomable=true %}
        <div class="caption">
            CNG Auction Listing for Sawhill Colosseum Sestertius - September 20, 2023
        </div>
    </div>
</div>



The [1979 sale of Dr. Sawhill's collection](https://archive.org/details/ancientforeignco1979stac) by Stack's and Bowers was considered a "major sale,"[^1] and "many of the coins from the Sawhill Collection found their way into historically important collections."[^2] The sale included over 1,300 items, but most notably, 265 Ancient Roman and Greek coins from the Massachusetts Historical Society owned by [President John Quincy Adams](https://archive.org/details/partimassachuset1971stac) and his descendants were sold; this acquisition represented more than one-quarter of the total sale and consisted heavily of Roman Republican coinage[^3].

While a boon to collectors, the sale of Sawhill's collection represents a distinct cultural and academic loss for James Madison University. In order to better understand our past and protect our future, the Recovering Sawhill Project seeks to track the major collections and sales in which Sawhill coins have appeared. Below is a table enumerating our latest research in finding these objects. Lot numbers containing a decimal point indicate a particular coin within a multi-coin lot. For example, lot 98.2 refers to the second coin in lot 98, which originally contained four coins.

**Do you have a Sawhill coin or know where one might reside?** If so, please contact the [Curator of Coins for the Madison Art Collection](https://www.jmu.edu/madisonart/people/forsyth-jason.shtml). It is our desire to quantify the scale of Dr. Sawhill's numismatic contributions. In doing so, we will better understand our history, enhance the present collection, and protect it going forward.

### Table of Recent Sawhill Coin Sales
<table id="table" 
  data-toggle="table" 
  data-url="{{ '/assets/json/sawhill-temp.json' | relative_url }}"
  data-pagination="true"
  data-search="true"
  data-page-size="10"
  data-sort-name="1979 Sawhill Lot Number"
  data-sort-order="asc"
>
  <thead>
    <tr>
      <th data-field="1979 Sawhill Lot Number" data-sortable="true" data-align="center" data-width="5%">Lot</th>
      <th data-field="1979 Sawhill Description" data-sortable="true" data-width="55%">Sawhill Description</th>
      <th data-field="Provenance" data-sortable="true" data-width="32%" data-formatter="provenanceFormatter">Provenance</th>
      <th data-field="Date Recorded" data-sortable="true" data-align="center" data-formatter="dateFormatter" data-width="5%">Date</th>
      <th data-field="Persistent URL" data-formatter="urlFormatter" data-align="center" data-width="3%">Link</th>
      
    </tr>
  </thead>
</table>

<script>
function dateFormatter(value) {
    if (!value) return '';
    return new Date(value).toLocaleDateString('en-US', { 
        year: 'numeric', 
        month: 'short', 
        day: 'numeric' 
    });
}

function urlFormatter(value) {
    if (!value) return '';
    return '<a href="' + value + '" target="_blank"><i class="fas fa-external-link-alt"></i></a>';
}

function provenanceFormatter(value) {
    if (!value) return '';
    if (Array.isArray(value)) {
        return value.map(item => '• ' + item).join('<br>');
    }
    return value;
}
</script>

## References

[^1]: [CoinWeek: "Harvey Stack – Growing up in a Numismatic Family: The History of Stack’s – 1979"](https://coinweek.com/harvey-stack-growing-up-in-a-numismatic-family-the-early-days-of-stacks-1979/)

[^2]: [Stacks's and Bowers: "Harvey Stack Remembers: Growing up in a Numismatic Family, Part 78"](https://stacksbowers.com/harvey-stack-remembers-part-78/)

[^3]: [Conservatori Coins: Collection of Sale Catalogs](https://conservatoricoins.com/sale-catalogs/#sawhill)