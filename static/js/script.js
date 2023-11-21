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

document.getElementById('register-button-modal').addEventListener('click', function () {
    window.location.href = 'register.html';
});

/* Delete Promotions */
function confirmDelete() {
    if (confirm("Are you sure you want to delete this promotion?")) {
        document.getElementById('delete-form').submit();
    } else {
        event.preventDefault();
    }
}

/* updateDescription */

function updateDescription() {
    if (confirm("Are you sure you want to update promotions description?")) {
        document.getElementById('update-promo-description').submit();
    } else {
        event.preventDefault();
    }
}

/*Apply automatic filtering in recommended page */

$(document).ready(function () {
    $('input[name="filter-checkbox"]').on('change', function () {
        $(this).closest('form').submit();
    });
});

/*Implement search functionality in recommended page*/
$(document).ready(function () {
    $('#searhailment').on('input', function () {
        var searchText = $(this).val().toLowerCase();
        $('.filter-checkbox').each(function () {
            var ailmentName = $(this).next('label').text().toLowerCase();
            var parentDiv = $(this).closest('div');
            if (ailmentName.includes(searchText)) {
                parentDiv.show();
            } else {
                parentDiv.hide();
            }
        });
    });
});

/*Add checkbox remain checked in recommended*/
document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('ailment-filter-form');
    const checkboxes = form.querySelectorAll('.filter-checkbox');
  
    const updateCheckboxState = () => {
      const checkboxes = form.querySelectorAll('.filter-checkbox');
      checkboxes.forEach(checkbox => {
        localStorage.setItem(checkbox.value, checkbox.checked ? 'true' : 'false');
      });
    };
  
    checkboxes.forEach(function(checkbox) {
      const savedValue = localStorage.getItem(checkbox.value) || 'false';
      checkbox.checked = savedValue === 'true';
  
      checkbox.addEventListener('change', function() {
        updateCheckboxState();
      });
    });
  
    const clearAllButton = document.getElementById('clear-all-button');
    clearAllButton.addEventListener('click', () => {
      checkboxes.forEach(checkbox => {
        checkbox.checked = false;
        updateCheckboxState();
      });

      form.submit();
    });
  });





/*Implement clear active search functionality */