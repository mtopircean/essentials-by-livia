/* Promotions dropdown details section 
Reads, toggles visibility and changes the toggle icon*/

$(document).ready(function () {

    var isDetailsVisible = false;
    $("#detailsArea").hide()

    $(".btn-link").click(function () {
        $("#detailsArea").slideToggle();
        isDetailsVisible = !isDetailsVisible;

        $(".toggle-icon").html(isDetailsVisible ? '&#11165;' : '&#11167;');
    });
})

/* Recommandation tool page drop down filter 
Initialize, set initial status, toggle visibility, 
change toggle icon, change toggle icon based on screensize
*/

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

/* Expandeble section in profile page 
Initialize, set status as hidden, toggle icon and visibility
*/

$(document).ready(function () {

    var isDetailsVisible = false;
    $("#user-details").hide()

    $(".toggle-details").click(function () {
        $("#user-details").slideToggle();
        isDetailsVisible = !isDetailsVisible;

        $(".toggle-icon").html(isDetailsVisible ? '&#11165;' : '&#11167;');
    });
})

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

/*Add checkbox remain checked in recommended
Retrieves form and checkboxes
Updates local storage status, submits the form
Incorporates also the clear all button and functionality
*/

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('ailment-filter-form');
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

        form.submit();
    });
});