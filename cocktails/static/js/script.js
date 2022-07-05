$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $(".collapsible").collapsible();
    $('.carousel').carousel({
        numVisible: 4,
    });
    $('select').formSelect();

    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});


// add and remove other ingredients
let new_input = document.getElementById('new-input');
let add_other_btn = document.getElementById('add-other-btn');
let remove_other_btn = document.getElementById('remove-other-btn');

add_other_btn.onclick = function() {
    var newIngredient = document.createElement('input');
    newIngredient.setAttribute('name', 'other_ingredient');
    newIngredient.setAttribute('minlength', '2');
    newIngredient.setAttribute('max-length', '20');
    newIngredient.setAttribute('class', 'js-remove-test remove-other-btn validate');
    newIngredient.setAttribute('type', 'text');
    newIngredient.setAttribute('placeholder', 'Add more ingredients and measurements');
    newIngredient.required = true;
    new_input.appendChild(newIngredient);
    remove_other_btn.classList.remove("hide")
};

remove_other_btn.onclick = function() {
    var input_count = new_input.getElementsByClassName('js-remove-test');
    var btn_count = new_input.getElementsByClassName('remove-other-btn');
    if(input_count.length > 1) {
        new_input.removeChild(input_count[(input_count.length) - 1]);
        if(input_count.length = 1 && btn_count.length < 1) {
            remove_other_btn.classList.add("hide");
        };
    }
};