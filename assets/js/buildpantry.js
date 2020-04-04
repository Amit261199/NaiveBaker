// Create a "close" button and append it to each list item
var options=document.getElementsByClassName("list")
var optionArray=[]
for (var j=0;j<options.length;j++)
{
  optionArray.push(options[j].value);
}
var myNodelist = document.getElementById("ingList").getElementsByTagName("LI");
var Names=[];
var i;
for (i = 0; i < myNodelist.length; i++) {
  var span = document.createElement("SPAN");
  var hiddenElement = document.createElement("input");
  hiddenElement.setAttribute("type", "hidden");
  hiddenElement.setAttribute("name", "ing");
  hiddenElement.setAttribute("id", "hiddenElement");
  hiddenElement.setAttribute("value", myNodelist[i].textContent);
  Names.push(myNodelist[i].textContent)
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  myNodelist[i].appendChild(hiddenElement);
  myNodelist[i].appendChild(span);
}


// Click on a close button to hide the current list item
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var p=this.parentElement.textContent
    function checkcurrent(name){
      if (p===name)
      {
        return true;
      }
      else return false;
    }
    Names.splice(Names.findIndex(checkcurrent),1)
    this.parentElement.remove();
  }
}

// Add a "checked" symbol when clicking on a list item
var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('checked');
  }
}, false);

// Create a new list item when clicking on the "Add" button
function newElement() {

  var names=[]
  var li = document.createElement("li");
  var inputValue = document.getElementById("myInput").value;
  var t = document.createTextNode(inputValue);
  var hiddenElement = document.createElement("input");
  hiddenElement.setAttribute("type", "hidden");
  hiddenElement.setAttribute("name", "ing");
  hiddenElement.setAttribute("id", "hiddenElement");
  hiddenElement.setAttribute("value", inputValue);
  li.appendChild(t);
  li.appendChild(hiddenElement);
 
  if (inputValue === '') {
    alert("You must write something!");
  }else if(!optionArray.includes(inputValue)){
    alert("please enter a valid ingredient");
  }
  else if(Names.includes(inputValue)){
    alert(inputValue+" is already added to the list");
  }
   else {
    document.getElementById("ingList").appendChild(li);
    Names.push(inputValue)
  }
  document.getElementById("myInput").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);
  
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var p=this.parentElement.textContent
      function checkcurrent(name){
      if (p===name)
      {
        return true;
      }
      else return false;
    }
    Names.splice(Names.findIndex(checkcurrent),1)
      this.parentElement.remove();
    }
  }
}


function openWins(){
  window.open("recipedisplay.html");
}

