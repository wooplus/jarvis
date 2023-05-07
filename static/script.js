console.log("hello");

let data = [
  {
    subject:
      "Keydous NJ68 Pro Hot Swappable Keyboard, SMSL VMV D1se MQA USB DAC, Xduoo XD-05 Plus DAC/Amp and more...",
    sender: "Drop",
    date: "Sun, 07 May 2023 06:04:43 +0000",
  },
  {
    subject: "",
    sender: "Twitter",
    date: "Sun, 07 May 2023 14:37:48 +0000",
  },
  {
    subject: "Big Savings Beyond This Point =?UTF-8?Q?=F0=9F=9A=B8?=",
    sender: "SHEIN",
    date: "Sun, 7 May 2023 17:34:20 +0200",
  },
];

document.getElementById("play-btn").addEventListener("click", () => {
  // fetching data
  fetch("/convert-to-speech", {
    method: "POST",
  })
    .then((response) => {
      // Handle the response from the Flask route
      console.log(response);
    })
    .catch((error) => {
      console.error(error);
    });
  document.getElementById("results-container").innerHTML = "";
  console.log("click");
  document.getElementById("results-container").style.display = "block";
  for (let i = 0; i < data.length; i++) {
    document.getElementById(
      "results-container"
    ).innerHTML += `<div class="gmail-container">
        <div class="title">
          <h3 class="email-title">${data[i].sender}</h3>
          <span class="email-date">${data[i].date}</span>
        </div>
        <div class="desc">
          <p>
            ${data[i].subject}
          </p>
        </div>
      </div>`;
  }
});
