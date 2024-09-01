function onRegisterButtonClick() {
  const name = document.getElementById("user_name").value;
  const gender =
    document.getElementById("user_gender").value == "male" ? true : false;
  const debit_card_number = parseFloat(
    document.getElementById("user_debit_card_name").value,
  );
  const email = document.getElementById("user_email").value;

  const url = "http://localhost:8000/users/new/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: name,
      gender: gender,
      debit_card_number: debit_card_number,
      email: email,
    }),
  })
    .then((response) => response.text())
    .then((text) => JSON.parse(text))
    .then((json) => json.user_id)
    .then((user_id) => sessionStorage.setItem("user_id", user_id.toString()))
    .catch((error) => console.log(error));
  window.location.replace("http://localhost:8000/hello/");
}
