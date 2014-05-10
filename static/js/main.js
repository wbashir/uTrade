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
String.prototype.toProperCase = function () {
    var words = this.split(' ');
    var results = [];
    for (var i = 0; i < words.length; i++) {
        var letter = words[i].charAt(0).toUpperCase();
        results.push(letter + words[i].slice(1));
    }
    return results.join(' ');
};

/**
 *
 */
function reloadSelectItem() {
    $.ajax({
        url: "/get_all_books",
        dataType: 'json',
        success: function (data) {
            $.each(data.items, function (i, value) {
                $('#bookList').append($('<option>').text(value.title.toProperCase()).attr('value', value.id));
            });

        }
    });
}

$(document).ready(function () {
    reloadSelectItem();

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


    $('#new-book').click(function (e) {
        e.preventDefault();
        $('#myModal').modal();
    });

    $('#save-item').click(function (e) {
        e.preventDefault();
        var itemForm = $('#new-book-form');
        var jsonObj = parseForm(itemForm);

        $.ajax({
            url: '/create/item',
            type: 'post',
            contentType: 'application/json',
            data: JSON.stringify(jsonObj),
            success: function (data) {
                window.location.replace("/create/posting");
                reloadSelectItem();
            },
            error: function (xhr, textStatus, thrownError) {
                console.log(thrownError);
            }
        });

    });
    $('#save-posting').click(function (e) {
        e.preventDefault();
        var postingForm = $('#posting-form');
        var jsonObj = parseForm(postingForm);

        $.ajax({
            url: '/create/posting',
            type: 'post',
            contentType: 'application/json',
            data: JSON.stringify(jsonObj),
            success: function (data) {
                window.location.replace("/");
            },
            error: function (xhr, textStatus, thrownError) {
                console.log(thrownError);
            }
        });
    });

    $('.delete-opt').click(function (e) {
        e.preventDefault();
        var par = $(e.target).parent();
        var id = par.attr('id').split('-')[1];
        var urlToDelete = '/delete/posting/' + id

        $.ajax({
            url: urlToDelete,
            type: 'DELETE',
            success: function (result) {
                window.location.replace("/");
                reloadSelectItem();
            }
        });
    });

//    $("select").select2({
//        placeholder: "Select a Book",
//        allowClear: true
//    });
});