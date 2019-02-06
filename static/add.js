

function sideLoad() {
    document.getElementById("sidebar-mobile").style.width= "50%";
    document.body.style.backgroundColor="rgba(0,0,0,0.4)";
}

function sideClose() {
    document.getElementById("sidebar-mobile").style.width= "0";
    document.body.style.backgroundColor="white";
}

// Wrap every letter in a span
$('.opening .letters').each(function(){
    $(this).html($(this).text().replace(/([^\x00-\x80]|\w)/g, "<span class='letter'>$&</span>"));
  });
  
  anime.timeline({loop: false})
    .add({
      targets: '.opening .letter',
      scale: [0, 1],
      duration: 1500,
      elasticity: 600,
      delay: function(el, i) {
        return 45 * (i+1)
      }
    }).add({
      targets: '.ml9',
      opacity: 0,
      duration: 1000,
      easing: "easeOutExpo",
      delay: 1000
    });