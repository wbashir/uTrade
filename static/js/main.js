requirejs.config({
    baseUrl: "/static/",
    paths: {
        lodash: "bower_components/lodash/dist/lodash.min",
        jquery: "bower_components/jquery/dist/jquery.min",
        ui: "js/ui",
        data: "js/data",
        mixins: "js/mixins"
    }
});

requirejs(["lodash", "jquery"], function (_) {

    var baseURL = $(this).data("url");
    $.ajax({
        url: "/get_all_books",
        dataType: 'json',
        success: function (data) {

            $.each(data, function(i, value) {
             $('#taxList').append($('<option>').text(value).attr('value', value));
            });

        }
    });
});
