var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var imgs = document.getElementsByClassName("carousel-images");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
var i;
for(i=0;i<imgs.length;i++){
    imgs[i].onclick = function(){
        modal.style.display = "block";
        modalImg.src = this.src;
        captionText.innerHTML = this.alt;
        var inds=document.getElementsByClassName("carousel-indicators")
        inds[0].classList.add('d-none')
        
      }
}


// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
  var inds=document.getElementsByClassName("carousel-indicators")
  inds[0].classList.remove('d-none')
  
} 