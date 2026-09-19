with open("assets/css/style.css", "r") as f:
    css = f.read()

# Let's add ONLY the specific macOS dock hover effect the user requested on the `.navbar-list` and `.navbar-item`.
# The user wants "collapse them into smaller parts and when we hover over them they become bigger just like macbook's icons list in the botton".
# To achieve this gracefully without messing up the entire media query structure of the template:

custom_css = """
/* Macbook dock style hover effect */
@media (min-width: 768px) {
  .navbar-list {
    display: flex;
    align-items: flex-end;
    gap: 10px !important;
  }

  .navbar-link {
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    transform-origin: bottom center;
    padding: 10px 8px !important;
    font-size: 13px !important;
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
    f.write(custom_css)
