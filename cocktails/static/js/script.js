$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $(".collapsible").collapsible();
    $('.carousel').carousel({
        numVisible: 4,
    });
    $('select').formSelect();
    $('.modal').modal();

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

// variables related to add and remove 'method'
let new_method = document.getElementById('new-method');
let add_meth_btn = document.getElementById('add-meth-btn');
let remove_meth_btn = document.getElementById('remove-meth-btn');
let maximum = 8;
let remove_meth = document.getElementsByClassName('remove-meth');
let tally = remove_meth.length

if (tally === 1) {
    remove_meth_btn.classList.add("disabled");
};

// adding a new input for 'method'
// a maximum of 8 inputs are possible
// if the user attempts to add more than 8, an error msg appears on-screen
add_meth_btn.onclick = function() {
    if (tally === maximum) {
        var errorMethod = document.createElement('p');
        errorMethod.setAttribute('id', 'error-method');
        errorMethod.innerHTML = "Maximum number of steps reached";
        errorMethod.style.textAlign = "center";
        new_method.appendChild(errorMethod);
        add_meth_btn.classList.add("disabled");
    } else {
    var newMethod = document.createElement('input');
    newMethod.setAttribute('name', 'method');
    newMethod.setAttribute('minlength', '5');
    newMethod.setAttribute('max-length', '75');
    newMethod.setAttribute('class', 'remove-meth remove-meth-btn validate');
    newMethod.setAttribute('type', 'text');
    newMethod.setAttribute('placeholder', 'Add another step');
    newMethod.required = true;
    new_method.appendChild(newMethod);
    remove_meth_btn.classList.remove("disabled");
    tally++;
    console.log(tally);
    }
};

// removing the previous input for 'method'
remove_meth_btn.onclick = function() {
    var remove_meth = new_method.getElementsByClassName('remove-meth');
    var error_method = document.getElementById('error-method');
    if(tally > 1) {
        new_method.removeChild(remove_meth[(tally) - 1]);
        if (tally === maximum) {
            if (document.contains(error_method)) {
                error_method.remove();
                add_meth_btn.classList.remove("disabled");
            }
            add_meth_btn.classList.remove("disabled");
        } else if (tally === 2) {
            remove_meth_btn.classList.add("disabled");
        } else {
            remove_meth_btn.classList.remove("disabled");
        }
    }
    tally--;
    console.log(tally);
};

// variables related to add and remove 'other ingredients'
let new_input = document.getElementById('new-input');
let add_other_btn = document.getElementById('add-other-btn');
let remove_other_btn = document.getElementById('remove-other-btn');
let max = 8;
let js_remove_test = document.getElementsByClassName('js-remove-test');
let counter = js_remove_test.length

if (counter === 1) {
    remove_other_btn.classList.add("disabled");
};

// adding a new input for 'other ingredients'
// a maximum of 8 inputs are possible
// if the user attempts to add more than 8, an error msg appears on-screen
add_other_btn.onclick = function() {
    if (counter === max) {
        var errorFlash = document.createElement('p');
        errorFlash.setAttribute('id', 'error-flash');
        errorFlash.innerHTML = "Max reached";
        errorFlash.style.textAlign = "center";
        new_input.appendChild(errorFlash);
        add_other_btn.classList.add("disabled");
    } else {
    var newIngredient = document.createElement('input');
    newIngredient.setAttribute('name', 'other_ingredient');
    newIngredient.setAttribute('minlength', '2');
    newIngredient.setAttribute('max-length', '20');
    newIngredient.setAttribute('class', 'js-remove-test remove-other-btn validate');
    newIngredient.setAttribute('type', 'text');
    newIngredient.setAttribute('placeholder', 'Add more ingredients and measurements');
    newIngredient.required = true;
    new_input.appendChild(newIngredient);
    remove_other_btn.classList.remove("disabled");
    counter++;
    console.log(counter);
    }
};

// removing the previous input for 'other ingredients'
remove_other_btn.onclick = function() {
    var js_remove_test = new_input.getElementsByClassName('js-remove-test');
    var error_flash = document.getElementById('error-flash');
    if(counter > 1) {
        new_input.removeChild(js_remove_test[(counter) - 1]);
        if (counter === max) {
            if (document.contains(error_flash)) {
                error_flash.remove();
                add_other_btn.classList.remove("disabled");
            }
            add_other_btn.classList.remove("disabled");
        } else if (counter === 2) {
            remove_other_btn.classList.add("disabled");
        } else {
            remove_other_btn.classList.remove("disabled");
        }
    }
    counter--;
    console.log(counter);
};