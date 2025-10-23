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
          description: "Faculty and Students in the COIN Research Group",
          section: "Navigation",
          handler: () => {
            window.location.href = "/people/";
          },
        },{id: "post-coin-identification-with-deep-metric-learning",
        
          title: "Coin Identification with Deep Metric Learning",
        
        description: "Jackson Greer (CS &#39;25) presents at JMU CS Research Day",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/jackson/";
          
        },
      },{id: "books-the-godfather",
          title: 'The Godfather',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/the_godfather/";
            },},{id: "news-site-launch",
          title: 'Site Launch!',
          description: "",
          section: "News",},{id: "projects-coin-attribution",
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
