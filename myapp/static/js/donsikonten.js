document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.donation-btn-group button');
    const customAmountInput = document.getElementById('customAmount');
    const anonymousCheckbox = document.getElementById('anonymousDonation');
    const donorNameInput = document.getElementById('donorName');

    // Fungsi tombol nominal
    buttons.forEach(button => {
      button.addEventListener('click', function () {
        buttons.forEach(btn => btn.classList.remove('active'));
        this.classList.add('active');
        const amount = this.getAttribute('data-amount');
        customAmountInput.value = `Rp. ${parseInt(amount).toLocaleString()}`;
      });
    });

    // Fungsi checkbox anonim
    anonymousCheckbox.addEventListener('change', function () {
      if (this.checked) {
        donorNameInput.value = '';
        donorNameInput.disabled = true;
      } else {
        donorNameInput.disabled = false;
      }
    });
  });