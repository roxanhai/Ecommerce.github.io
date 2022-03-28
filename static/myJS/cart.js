//Cập nhật Order của Customer
function updateUserOrder(productID, actions) {
  console.log("User is logged in, sending data");
  var url = "/add_to_cart/"; //path in 'store/urls.py'
  // fetch is an API
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productID, actions: actions }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("data:", data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

//Thêm-Xoá Product được chọn vào Cart (Tuỳ theo Action được truyền)
var updateBtn = document.getElementsByClassName("add-to-cart");
for (var i = 0; i < updateBtn.length; i++) {
  //updateBtn.length = Số lượng các btn chứa class "add-to-cart" trong trang html
  updateBtn[i].addEventListener("click", function () {
    //product_id & actions Được khai báo tương ứng với data-product_id và data-action
    var productID = this.dataset.product_id;
    var actions = this.dataset.action;
    console.log("product_id:", productID, " action:", actions);
    if (user == "AnonymousUser") {
      console.log("Not logged in");
      window.location.href = "/login/";
    } else {
      console.log(user);
      updateUserOrder(productID, actions);
      window.location.reload(); //Reload page
    }
  });
}
