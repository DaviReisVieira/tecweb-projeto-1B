// Filter Post-Its
filterSelection("all");
function filterSelection(filterName) {
  var liArray = [];
  liArray = document.getElementsByClassName("filterDiv");
  if (filterName == "all") filterName = "";
  [].slice.call(liArray).forEach((li) => {
    removeElements(li, "show");
    if (li.className.indexOf(filterName) > -1) showFilteredElements(li, "show");
  });
}

function showFilteredElements(element, name) {
  var class1, class2;
  class1 = element.className.split(" ");
  class2 = name.split(" ");
  for (var i = 0; i < class2.length; i++) {
    if (class1.indexOf(class2[i]) == -1) {
      element.className += " " + class2[i];
    }
  }
}

function removeElements(element, name) {
  var class1, class2;
  class1 = element.className.split(" ");
  class2 = name.split(" ");
  for (var i = 0; i < class2.length; i++) {
    while (class1.indexOf(class2[i]) > -1) {
      class1.splice(class1.indexOf(class2[i]), 1);
    }
  }
  element.className = class1.join(" ");
}

// Botão ativo
var btnContainer = document.getElementById("buttonFilterContainer");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function () {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}
