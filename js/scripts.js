const reviewList = [
  "Tim\n\n" + "Great company quick delivery\n\n" + "",
  "Jess\n\n" +
    "My son's computer was excellent, and the delivery was prompt and fantastic\n\n" +
    "",
  "Hassan\n\n" + "One of the best companies I have ordered from\n\n" + "",
];

function displayReviews(reviewList) {
  const textBox = document.createElement("textarea");
  textBox.classList.add("text-box");
  textBox.readOnly = true;

  let currentIndex = 0;

  function showReview() {
    textBox.value = reviewList[currentIndex];
    currentIndex = (currentIndex + 1) % reviewList.length;
  }

  showReview();
  setInterval(showReview, 2000);

  document.body.appendChild(textBox);
}

displayReviews(reviewList);
