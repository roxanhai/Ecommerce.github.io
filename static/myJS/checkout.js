//Phần Form trong Checkout
var form = document.getElementById("form");
form.addEventListener("submit", function (event) {
  //Chưa hiểu lý do thêm vào
  event.preventDefault();
  console.log("Form submitted...");
  document.getElementById("form-button").classList.add("hidden");
  document.getElementById("payment-info").classList.remove("hidden");

  // Code cho nút Payment tự tạo
  // document
  //   .getElementById("make-payment")
  //   .addEventListener("click", function (event) {
  //     submitFormData();
  //   });
});

// var userFormData = {
//   name: user.customer,
//   email: null,
//   total: total,
// };
// var shippingFormData = {
//   address: null,
//   city: null,
//   state: null,
//   zipcode: null,
//   country: null,
// };
// function submitFormData() {
//   console.log("Payment button clicked");
//   if (shipping != false) {
//     shippingFormData.address = form.address.value;
//     shippingFormData.city = form.city.value;
//     shippingFormData.state = form.state.value;
//     shippingFormData.zipcode = form.zipcode.value;
//     shippingFormData.country = form.country.value;
//   }

//   if (user == "AnonymousUser") {
//     userFormData.name = form.name.value;
//     userFormData.email = form.email.value;
//   }
//   console.log(shippingFormData);
//   console.log(userFormData);
//   fetch("/payment_order/", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//       "X-CSRFToken": csrftoken,
//     },
//     body: JSON.stringify({
//       userFormData: userFormData,
//       shippingFormData: shippingFormData,
//     }),
//   })
//     .then((response) => {
//       return response.json();
//     })
//     .then((data) => {
//       console.log("Success:", data);
//       alert("Transation completed");
//       window.location.href = "/";
//     });
// }
