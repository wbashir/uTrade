//requirejs.config({
//    baseUrl: "/static/",
//    paths: {
//        lodash: "bower_components/lodash/dist/lodash.min",
//        jquery: "bower_components/jquery/jquery.min",
//        ui: "js/ui",
//        data: "js/data",
//        mixins: "js/mixins"
//    }
//});

//requirejs(["lodash", "jquery"], function () {
//
//
//    $.ajax({
//        url: "/get_all_books",
//        dataType: 'json',
//        success: function (data) {
//            $.each(data.items, function (i, value) {
//                $('#taxList').append($('<option>').text(value.title + value.description).attr('value', value.id));
//            });
//
//        }
//    });
//});

$(document).ready(function () {


    /**
     *
     * @param form
     * @return {Object}
     */
    function parseForm(form) {
        var fields = {};
        var fieldArray = $(form).serializeArray();

        _.each(fieldArray, function (field) {
            fields[field.name] = field.value;
        });

        return fields;
    }


    $.ajax({
        url: "/get_all_books",
        dataType: 'json',
        success: function (data) {
            $.each(data.items, function (i, value) {
                $('#bookList').append($('<option>').text(value.title).attr('value', value.id));
            });

        }
    });


    $('#save-posting').click(function (e) {
        e.preventDefault();
        var postingForm = $('#posting-form');
        var jsonObj = parseForm(postingForm);


        $.ajax({
            url: '/create/posting',
            type: 'post',
            contentType:'application/json',
            data: jsonObj,
            success: function (data) {
                console.log('success');
            },
            error: function (xhr, textStatus, thrownError) {
                console.log(thrownError);
            }
        });

    });

//    $("select").select2({
//        placeholder: "Select a Book",
//        allowClear: true
//    });
});