/** Promotions dropdown details section**/

$(document).ready(function () {

    var isDetailsVisible = false;
    $("#detailsArea").hide()

    $(".btn-link").click(function () {
        $("#detailsArea").slideToggle();
        isDetailsVisible = !isDetailsVisible;

        $(".toggle-icon").html(isDetailsVisible ? '&#11165;' : '&#11167;');
    });
})

/** Recommandation tool page drop down filter **/

$(document).ready(function () {
    var isAilmentListVisible = $(window).width() >= 768;
    $(".filter-content").show();

    $("#toggle-ailment-list").click(function () {
        $(".filter-content").slideToggle();
        isAilmentListVisible = !isAilmentListVisible;

        $("#toggle-ailment-list").html("Ailment list " + (isAilmentListVisible ? '&#11165;' :
            '&#11167;'));
    });

    $(window).resize(function () {
        isAilmentListVisible = $(window).width() < 768;

        if (!isAilmentListVisible) {
            $(".filter-content").hide();
        }

        $("#toggle-ailment-list").html("Ailment list " + (isAilmentListVisible ? '&#11165;' :
            '&#11167;'));
    });
});

/** Modal link to Register **/

document.getElementById('register-button').addEventListener('click', function() {
    window.location.href = 'register.html';
});

