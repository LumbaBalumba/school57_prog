async function onClick() {
  const name = document.getElementById("user_name").value;
  const gender =
    document.getElementById("user_gender").value == "male" ? true : false;
  const debit_card_number = parseFloat(
    document.getElementById("user_debit_card_name").value,
  );
  const email = document.getElementById("user_email").value;

  const url = "http://localhost:8000/users/new/";
  let response = await fetch(url, {
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
  });
  console.log(response.json());
}
