window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  console.log('from scrollFunction')
  if (document.body.scrollTop > 1 || document.documentElement.scrollTop > 1) {
    document.querySelector(".profile-background-img").style.height = "120px";

    // document.querySelector(".name").style.fontSize= "30px";

    document.querySelector(".profile-img").style.width= "100px";
    document.querySelector(".profile-img").style.minWidth= "100px";
    document.querySelector(".profile-img").style.left= "20px";
    // document.querySelector(".profile-img").style.bottom= "0px";

    document.querySelector(".profile-img img").style.border = "whitesmoke 4px solid";

    document.querySelector(".name").style.bottom = "4px";
    document.querySelector(".name").style.textAlign = "left";
    document.querySelector(".name").style.left = "130px";
  }
  else {
    document.querySelector(".profile-background-img").style.height = "210px";

    // document.querySelector(".name").style.fontSize= "60px";

    document.querySelector(".profile-img").style.width= "25%";
    document.querySelector(".profile-img").style.minWidth= "150px";
    document.querySelector(".profile-img").style.left= "6%";
    // document.querySelector(".profile-img").style.bottom= "-110px";

    document.querySelector(".profile-img img").style.border= "whitesmoke 7px solid";

    document.querySelector(".name").style.bottom = "10%";
    document.querySelector(".name").style.textAlign = "center";
    document.querySelector(".name").style.left = "25%";

  }
}