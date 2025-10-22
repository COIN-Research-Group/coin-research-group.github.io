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
          section: "News",},{id: "projects-3d-modeling-and-digital-twins",
          title: '3D Modeling and Digital Twins',
          description: "a project that redirects to another website",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_modeling/";
            },},{id: "projects-project-4",
          title: 'project 4',
          description: "another without an image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_scanning/";
            },},{id: "projects-project-5",
          title: 'project 5',
          description: "a project with a background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/5_tracking/";
            },},{id: "projects-coin-attribution",
          title: 'Coin Attribution',
          description: "Updating the Sawhill Collection with modern numismatic references",
          section: "Projects",handler: () => {
              window.location.href = "/projects/attribution/";
            },},{id: "projects-provenance-recovery",
          title: 'Provenance Recovery',
          description: "Finding the origins of the Sawhill Collection",
          section: "Projects",handler: () => {
              window.location.href = "/projects/provenance_recovery/";
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
