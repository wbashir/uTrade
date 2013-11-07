// Karma configuration
// Generated on Sun Oct 27 2013 14:30:28 GMT-0700 (PDT)

module.exports = function(config) {
  config.set({

    // base path, that will be used to resolve files and exclude
    basePath: "",


    // frameworks to use
    frameworks: ["jasmine"],


    // list of files / patterns to load in the browser
    files: [
      "app/static/bower_components/es5-shim/es5-shim.js",
      "app/static/bower_components/es5-shim/es5-sham.js",
      "app/static/bower_components/jquery/jquery.js",
      "app/static/bower_components/jasmine-jquery/lib/jasmine-jquery.js",
      "app/static/bower_components/jasmine-flight/lib/jasmine-flight.js",

      {pattern: "test-js/fixture/**/*.html", served: true, watched: true, included: false},

      // hack to load RequireJS after the shim libs
      "node_modules/karma-requirejs/lib/require.js",
      "node_modules/karma-requirejs/lib/adapter.js",

      // loaded with require
      {pattern: "app/static/bower_components/flight/**/*.js", included: false},
      {pattern: "app/static/js/**/*.js", included: false},
      {pattern: "test-js/spec/**/*.spec.js", included: false},

      "test-js/test-main.js"
    ],

    preprocessors: {
      "**/*.html": []
    },


    // list of files to exclude
    exclude: [
      "app/static/js/main.js"
    ],


    // test results reporter to use
    // possible values: "dots", "progress", "junit", "growl", "coverage"
    reporters: ["dots"],


    // web server port
    port: 9876,


    // enable / disable colors in the output (reporters and logs)
    colors: true,


    // level of logging
    // possible values: config.LOG_DISABLE || config.LOG_ERROR || config.LOG_WARN || config.LOG_INFO || config.LOG_DEBUG
    logLevel: config.LOG_INFO,


    // enable / disable watching file and executing tests whenever any file changes
    autoWatch: true,


    // Start these browsers, currently available:
    // - Chrome
    // - ChromeCanary
    // - Firefox
    // - Opera (has to be installed with `npm install karma-opera-launcher`)
    // - Safari (only Mac; has to be installed with `npm install karma-safari-launcher`)
    // - PhantomJS
    // - IE (only Windows; has to be installed with `npm install karma-ie-launcher`)
    browsers: ["Chrome"],


    // If browser does not capture in given timeout [ms], kill it
    captureTimeout: 60000,


    // Continuous Integration mode
    // if true, it capture browsers, run tests and exit
    singleRun: false,

    // Karma will report all the tests that are slower than given time limit (in
    // ms).
    reportSlowerThan: 500
  });
};
