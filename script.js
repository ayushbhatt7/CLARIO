function animateMeter(percent) {
  const fill = document.querySelector('.meter-fill');
  const text = document.querySelector('.meter-text');
  let current = 0;

  const interval = setInterval(() => {
    if (current >= percent) {
      clearInterval(interval);
    } else {
      current++;
      fill.style.width = current + '%';
      text.textContent = current + '%';
    }
  }, 20);
}

// Animate to 75%
animateMeter(75);