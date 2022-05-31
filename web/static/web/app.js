$(document).ready(handleScrollEnd);

function handleScrollEnd() {
  const currentScrollPosition = $(window).scrollTop();

  let $closestPage;
  let closestDistance = Infinity;

  $(".flex-work").each(function() {
    const $page = $( this );
    const distance = Math.abs(currentScrollPosition - getScrollTopFor($page));
    if(distance < closestDistance){
      closestDistance = distance;
      $closestPage = $page;
    }
  });

  window.lastClosestPage = $closestPage;
  chooseColor($closestPage);
}

function getScrollTopFor($page) {
  return $page.offset().top + 200;
}


let scrollTimer;
$(window).scroll(function() {
  //reset scrolltimer, to cancel running handleScrollEnd
  clearTimeout(scrollTimer);

  // wait 100ms before running handleScrollEnd
  scrollTimer = setTimeout(handleScrollEnd, 100);
});

function chooseColor($page){
  console.log("changing color to color for", $($page).find(".work").text());
  $('body').css({"--background-color": $($page).data("color")})
}
