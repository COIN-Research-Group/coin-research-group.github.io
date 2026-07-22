// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-blog",
          title: "blog",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/blog/";
          },
        },{id: "nav-projects",
          title: "projects",
          description: "Active projects in the COIN Research Group and the Madison Art Collection",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-people",
          title: "people",
          description: "Faculty, Students, and Alumni of the Recovering Sawhill Project",
          section: "Navigation",
          handler: () => {
            window.location.href = "/people/";
          },
        },{id: "dropdown-black-cabinet",
              title: "Black Cabinet",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/black-cabinet/";
              },
            },{id: "post-student-presentations-on-deep-metric-learning-for-coin-identification",
        
          title: "Student Presentations on Deep Metric Learning for Coin Identification",
        
        description: "Trevor Schonbrun and Dhanshree Atre present research on ancient coin identification at regional conferences",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/student-presentations/";
          
        },
      },{id: "post-x-ray-imaging-to-identify-ancient-fakes",
        
          title: "X-ray Imaging to Identify Ancient Fakes",
        
        description: "A collaboration with the Madison Accelerator Lab helps identify fourrées in the collection",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/xray-mal/";
          
        },
      },{id: "post-sawhill-lot-1063-adams-lot-231-recovered",
        
          title: "Sawhill Lot 1063 / Adams Lot 231 Recovered!",
        
        description: "The Madison Art Collection has reacquired a coin from the Sawhill and Adams Collection.",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/sawhill-1063-mhs-231-recovered/";
          
        },
      },{id: "projects-coin-attribution",
          title: 'Coin Attribution',
          description: "Updating the Sawhill Collection with modern numismatic references",
          section: "Projects",handler: () => {
              window.location.href = "/projects/attribution/";
            },},{id: "projects-3d-modeling-and-fabrication",
          title: '3D Modeling and Fabrication',
          description: "Accessible models for research and outreach",
          section: "Projects",handler: () => {
              window.location.href = "/projects/modeling/";
            },},{id: "projects-provenance-recovery",
          title: 'Provenance Recovery',
          description: "Uncovering the origins of the Sawhill Collection",
          section: "Projects",handler: () => {
              window.location.href = "/projects/provenance_recovery/";
            },},{id: "projects-auction-catalog-digitization",
          title: 'Auction Catalog Digitization',
          description: "The source material for recovering Sawhill",
          section: "Projects",handler: () => {
              window.location.href = "/projects/scanning/";
            },},{id: "projects-tracking-sawhill",
          title: 'Tracking Sawhill',
          description: "Following Sawhill&#39;s coins from 1979 to the present",
          section: "Projects",handler: () => {
              window.location.href = "/projects/tracking/";
            },},{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
