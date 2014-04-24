requirejs.config({
  baseUrl: "/static/",
  paths: {
    lodash: "bower_components/lodash/dist/lodash.min",

    ui: "js/ui",
    data: "js/data",
    mixins: "js/mixins"
  }
});

requirejs(["lodash"], function (_) {
  
});
