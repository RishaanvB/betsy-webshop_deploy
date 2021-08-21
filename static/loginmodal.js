const displayModalOnFormFailure = () => {
  const loginModal = new bootstrap.Modal(
    document.getElementById("loginModalToggle"),
    {
      keyboard: true,
    }
  );
  const registerModal = new bootstrap.Modal(
    document.getElementById("registerModalToggle"),
    {
      keyboard: true,
    }
  );

  const checkLogin = document.getElementById("checklogin");
  const checkRegister = document.getElementById("checkregister");
  if (checkRegister && !checkLogin) {
    registerModal.show();
  }
  if (!checkRegister && checkLogin) {
    loginModal.show();
  }
};

displayModalOnFormFailure();
