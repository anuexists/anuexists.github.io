with open("assets/css/style.css", "r") as f:
    css = f.read()

# Make the mac dock effect smoother and more pronounced
custom_css3 = """
/* Macbook dock style hover effect */
@media (min-width: 1024px) {
  .navbar-list {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .navbar-link {
    transform-origin: bottom center;
  }

  .navbar-item:hover .navbar-link {
    transform: scale(1.3) translateY(-2px);
    color: var(--orange-yellow-crayola) !important;
    z-index: 10;
    position: relative;
  }

  /* Adjacent siblings scale up slightly */
  .navbar-item:hover + .navbar-item .navbar-link,
  .navbar-item:has(+ .navbar-item:hover) .navbar-link {
    transform: scale(1.15) translateY(-1px);
    color: var(--light-gray) !important;
  }
}
"""

with open("assets/css/style.css", "a") as f:
    f.write(custom_css3)
