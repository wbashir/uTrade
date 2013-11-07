module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON("package.json"),
    less: {
      development: {
        files: [
          {
            expand: true,     // Enable dynamic expansion.
            cwd: "app/static/less/",      // Src matches are relative to this path.
            src: ["**/*.less"], // Actual pattern(s) to match.
            dest: "app/static/css/",   // Destination path prefix.
            ext: ".css"   // Dest filepaths will have this extension.
          }
        ]
      }
    },
    watch: {
      styles: {
        files: ["app/static/less/**/*.less"],
        tasks: ["less:development"],
        options: {
          spawn: false
        }
      }
    },
    karma: {
      unit: {
        configFile: 'karma.conf.js',
        browsers: ['PhantomJS']
      }
    }
  });

  grunt.loadNpmTasks("grunt-contrib-less");

  grunt.loadNpmTasks("grunt-contrib-watch");

  grunt.loadNpmTasks('grunt-karma');

  // Default task(s).
  grunt.registerTask("default", "less:development");

};
