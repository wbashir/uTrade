requirejs.config({
  baseUrl: "/static/",
  paths: {
    flight: "bower_components/flight/",
    lodash: "bower_components/lodash/dist/lodash.min",

    ui: "js/ui",
    data: "js/data",
    mixins: "js/mixins"
  }
});

requirejs(["lodash"], function (_) {
  
});
