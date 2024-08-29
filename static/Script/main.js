
// =======================swiper===============================
var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

  // =========================== questions ================================

  let questions = document.querySelectorAll('.question .title');
  let questionContainers = document.querySelectorAll('.question > .question_container');
  let pushMinus = document.querySelectorAll('.question span');
  let questionContents = document.querySelectorAll('.question .content');
  let heights = [];
  
  // heights 각 questionContainers의 높이 저장
  function contentsHight(){
      heights = [];
      questionContents.forEach((questionContent) => {
          let height = questionContent.offsetHeight;
          heights.push(height);
      });
  };
  contentsHight();
  
  // main 동작 코드
  let FAQ = [];
  questions.forEach((question, index) => {
      question.addEventListener('click', () => {
          if(!FAQ[index]){
              questionContainers[index].style.height = `${75 + heights[index]}px`;
              pushMinus[index].innerHTML = '+';
              pushMinus[index].style.fontSize = '35px';
              FAQ[index] = 1;
          }else{
              questionContainers[index].style.height = '75px';
              pushMinus[index].innerHTML = '-';
              pushMinus[index].style.fontSize = '50px';
              FAQ[index] = 0;
          };
      });
  });
  
  // 화면의 넓이에 따라 heights의 높이 갱신 및 questionContainers높이 조절
  window.addEventListener('resize', () => {
      contentsHight();
      for(let index = 0; index < questionContainers.length; index++){
          if(FAQ[index]) {
              questionContainers[index].style.height = `${75 + heights[index]}px`;
          };
      };
  });