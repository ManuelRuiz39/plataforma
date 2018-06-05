$('#openBtn').click(function () {
    $('#myModal').modal({ show: true })
}); $('#myTab a').click(function (e) {
    e.preventDefault();
    $(this).tab('show');
});

$(function () {
    $('#myTab a:last').tab('show');
})
$("[data-toggle=tooltip]").tooltip();
$("[data-toggle=popover]").popover();
$(".alert").delay(200).addClass("in").fadeOut(3500);

$(".alert").addClass("in").fadeOut(3500);

$('.typeahead').typeahead({
    source: function (typeahead, query) {
        /* put your ajax call here..
        return $.get('/typeahead', { query: query }, function (data) {
           return typeahead.process(data);
        });
        */
        return ['alpha', 'beta', 'bravo', 'delta', 'epsilon', 'gamma', 'zulu'];
    }
});
$("[rel='tooltip']").tooltip();

$('.thumbnail').hover(
    function () {
        $(this).find('.caption').slideDown(250); //.fadeIn(250)
    },
    function () {
        $(this).find('.caption').slideUp(250); //.fadeOut(205)
    }
); 