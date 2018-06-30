function im_ok(element, id) {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", jQuery("[name=csrfmiddlewaretoken]").val());
        }
    });

    $.ajax({
        url: 'api/v1/member/' + id + '/',
        type: 'PATCH',
        dataType: "json",
        data: JSON.stringify({id: id, should_be_contacted: false}),
        contentType: "application/json",
        success: function () {
            $('.button .circle h1').html('You rock!');
        }
    });
}


setTimeout(function () {
    $(".button").removeClass("active");
}, 300);

