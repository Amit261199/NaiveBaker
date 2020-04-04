function newItem1() {
  var item = document.getElementById("input1").value;
  var ul = document.getElementById("list1");
  var li = document.createElement("li");
  li.appendChild(document.createTextNode("- " + item));
  ul.appendChild(li);
  document.getElementById("input1").value = "";
  li.onclick = removeItem;
}

document.body.onkeyup = function(e) {
  if (e.keyCode == 13) {
    newItem1();
  }
};

function removeItem(e) {
  e.target.parentElement.removeChild(e.target);
}