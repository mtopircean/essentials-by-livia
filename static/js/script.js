/*jshint esversion: 6 */
/* global $ */

/* Promotions dropdown details section 
Reads, toggles visibility and changes the toggle icon*/

$(document).ready(function () {

    var isDetailsVisible = false;
    $("#detailsArea").hide();

    $(".btn-link").click(function () {
        $("#detailsArea").slideToggle();
        isDetailsVisible = !isDetailsVisible;

        $(".toggle-icon").html(isDetailsVisible ? '&#8645;' : '&#8645;');
    });
});

/* Recommandation tool page drop down filter 
Initialize, set initial status, toggle visibility, 
change toggle icon, change toggle icon based on screensize
*/

$(document).ready(function () {
    var isMobileView = $(window).width() < 768;
    var keyboardFocused = false;

    updateAilmentListVisibility(isMobileView);

    $("#toggle-ailment-list").click(function () {
        toggleAilmentList();
    });

    $("#searchailment").focus(function () {
        if (isMobileView && !isAilmentListVisible()) {
            toggleAilmentList();
            keyboardFocused = true;
        }
    });

    $("#searchailment").blur(function () {
        keyboardFocused = false;
    });

    $(window).resize(function () {
        if (!keyboardFocused) {
            isMobileView = $(window).width() < 768;
            updateAilmentListVisibility(isMobileView);
        }
    });

    function toggleAilmentList() {
        $(".filter-content").slideToggle();
    }

    function updateAilmentListVisibility(isMobile) {
        if (isMobile) {
            $(".filter-content").hide();
        } else {
            $(".filter-content").show();
        }
    }

    function isAilmentListVisible() {
        return $(".filter-content").is(":visible");
    }

    function updateToggleText() {
        var toggleSymbol = '&#8645;';
        $("#toggle-ailment-list").html("Ailment list " + toggleSymbol);
    }

    updateToggleText();
});

/* Expandeble section in profile page 
Initialize, set status as hidden, toggle icon and visibility
*/

$(document).ready(function () {

    var isDetailsVisible = false;
    $("#user-details").hide();

    $(".toggle-details").click(function () {
        $("#user-details").slideToggle();
        isDetailsVisible = !isDetailsVisible;

        $(".toggle-icon").html(isDetailsVisible ? '&#8645;' : '&#8645;');
    });
});

/* Modal link to Register
Redirect user to register page
*/

document.getElementById('register-button-modal').addEventListener('click', function () {
    window.location.href = 'register.html';
});

/* Delete Promotions 
Confirms user deletion action and acts as a safety measure
*/
function confirmDelete() {
    if (confirm("Are you sure you want to delete this promotion?")) {
        document.getElementById('delete-form').submit();
    } else {
        event.preventDefault();
    }
}

/* Update Promotion Description 
Confirms user update action and acts as a safety measure
*/

function updateDescription() {
    if (confirm("Are you sure you want to update the promotion description?")) {
        document.getElementById('update-promo-description').submit();
    } else {
        event.preventDefault();
    }
}

/* Delete Product 
Confirms user deletion action and acts as a safety measure
*/
function confirmProductDelete() {
    if (confirm("Are you sure you want to delete this product?")) {
        document.getElementById('delete-product').submit();
    } else {
        event.preventDefault();
    }
}

/* Update Product Description 
Confirms user update action and acts as a safety measure
*/

function updateProductDescription() {
    if (confirm("Are you sure you want to update the product description?")) {
        document.getElementById('save-product-description').submit();
    } else {
        event.preventDefault();
    }
}



/*Apply automatic filtering in recommended page 
Submits the form if a checkbox is changed
*/

$(document).ready(function () {
    $('input[name="filter-checkbox"]').on('change', function () {
        $(this).closest('form').submit();
    });
});

/*Implement search functionality in recommended page
Collects the input text
Collects the ailment name
Shows and hides the checkboxes based on search matching filter element
*/
$(document).ready(function () {
    $('#searchailment').on('input', function () {
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

/*Add checkbox remain checked in recommended
Retrieves form and checkboxes
Updates local storage status, submits the form
Incorporates also the clear all button and functionality
*/

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('ailment-filter-form');
    if (!form) {
        return;
    }
    const checkboxes = form.querySelectorAll('.filter-checkbox');

    const updateCheckboxState = () => {
        const checkboxes = form.querySelectorAll('.filter-checkbox');
        checkboxes.forEach(checkbox => {
            localStorage.setItem(checkbox.value, checkbox.checked ? 'true' : 'false');
        });
    };

    checkboxes.forEach(function (checkbox) {
        const savedValue = localStorage.getItem(checkbox.value) || 'false';
        checkbox.checked = savedValue === 'true';

        checkbox.addEventListener('change', function () {
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

/*Add to favourites
Prevents default action on click
Toggles favourite button and the favorite class/status
Finalizes by submitting the form
Used local storage to maintain status of favorited item on reload
Resets the check boxes if item is favorited or removed
*/

$(document).ready(function () {
    $('.add-to-favorites-btn').on('click', function (event) {
        event.preventDefault();

        var button = $(this);
        var form = button.closest('form');
        var productId = form.find('input[name="product_id"]').val();

        if (button.find('i').hasClass('fas')) {
            button.html('<i class="far fa-heart"></i> Add to Favorites');
        } else {
            button.html('<i class="fas fa-heart"></i> Remove from Favorites');
        }

        button.toggleClass('favorited');

        localStorage.setItem('favoriteActionOccurred', 'true');

        form.submit();
    });

    if (localStorage.getItem('favoriteActionOccurred') === 'true') {
        $('.filter-checkbox').prop('checked', false);
        localStorage.removeItem('favoriteActionOccurred');
    }
});

/* Update profile toast */
$(document).ready(function () {
    var toastTrigger = $('#toastTrigger');
    if (toastTrigger.length) {
        var message = toastTrigger.data('message');
        $('#profileActionToast .toast-body').text(message);
        $('#profileActionToast').toast('show');
    }
});

/* Delete account toast */

$(document).ready(function () {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('account_deleted') === 'true') {
        var toastEl = document.getElementById('deleteAccountToast');
        var toast = new bootstrap.Toast(toastEl);
        toast.show();
    }
});

/* Toast for changes to product section */
$(document).ready(function () {
    var toastTrigger = $('#toastTrigger');
    if (toastTrigger.length) {
        var message = toastTrigger.data('message');
        $('#productActionToast .toast-body').text(message);
        $('#productActionToast').toast('show');
    }
});


/* Toast for changes to promotion section */

$(document).ready(function () {
    var toastTrigger = $('#toastTrigger');
    if (toastTrigger.length) {
        var message = toastTrigger.data('message');
        $('#promotionActionToast .toast-body').text(message);
        $('#promotionActionToast').toast('show');
    }
});