/*!
 * Start Bootstrap - Shop Homepage v5.0.1 (https://startbootstrap.com/template/shop-homepage)
 * Copyright 2013-2021 Start Bootstrap
 * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
 */
// This file is intentionally blank
// Use this file to add JavaScript to your project
const calculateTotalPriceInCheckout = () => {
  const prices = document.querySelectorAll(".productPrice");
  const totalPriceCheckout = document.getElementById("totalPriceCheckout");
  let totalPrice = 0;
  prices.forEach((price) => {
    totalPrice += +price.innerHTML;
  });

  totalPriceCheckout.innerHTML = `€ ${totalPrice.toFixed(2)}`;
};

const displayTotalPricePerProduct = () => {
  const selectElements = document.querySelectorAll(".productAmountCheckout");
  selectElements.forEach((select) => {
    select.addEventListener("change", () => {
      const id = select.id.split("-").slice(-1);
      const totalSinglePrice = document.getElementById(`price-data-${id}`);
      const pricePerUnit = totalSinglePrice.getAttribute("data-price-per-unit");
      totalSinglePrice.innerText = `${(pricePerUnit * select.value).toFixed(
        2
      )}`;
      calculateTotalPriceInCheckout();
    });
  });
};

const displayTotalPriceinSideCart = () => {
  const productPricesInSideCart = document.querySelectorAll(
    ".product-price-per-unit.sidecart"
  );
  const totalPriceSideCart = document.getElementById("totalPriceSideCart");
  let totalPrice = 0;

  productPricesInSideCart.forEach((price) => {
    totalPrice += +price.innerHTML;
  });
  totalPriceSideCart.innerHTML = `Total: € ${totalPrice}`;
};

const handleCollapseAccountForms = () => {
  const collapseAccountBtn = document.getElementById("collapseAccountBtn");
  const collapseProductFormBtn = document.getElementById(
    "collapseProductFormBtn"
  );

  const collapseAccountForm = document.getElementById("collapseAccountForm");
  const collapseProductForm = document.getElementById("collapseProductForm");

  collapseProductFormBtn.addEventListener("click", () => {
    if (collapseAccountForm.classList.contains("show")) {
      collapseAccountForm.classList.remove("collapse");
      collapseAccountForm.classList.remove("show");
      collapseAccountForm.classList.add("collapsing");
    }
  });
  collapseAccountBtn.addEventListener("click", () => {
    if (collapseProductForm.classList.contains("show")) {
      collapseProductForm.classList.remove("collapse");
      collapseProductForm.classList.remove("show");
      collapseProductForm.classList.add("collapsing");
    }
  });
};
if (
  window.location.href.endsWith("account") ||
  window.location.href.endsWith("account/transactions")
) {
  handleCollapseAccountForms();
}

calculateTotalPriceInCheckout();
displayTotalPricePerProduct();
displayTotalPriceinSideCart();
