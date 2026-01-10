/* FILE PURPOSE: Toggle dark mode and persist preference across pages. */
/* # CAME FROM: dashboard/templates/dashboard/*.html -> includes this script. */

(() => {
  const storageKey = "dashboardTheme";
  const darkValue = "dark";
  const lightValue = "light";
  const button = document.getElementById("theme-toggle");
  const themeVars = {
    light: {
      "--bg-color": "#f7f9fb",
      "--text-color": "#1f2933",
      "--link-color": "#0b5fa5",
      "--table-head-bg": "#243b53",
      "--table-even-row": "#e4edf5",
      "--button-bg": "#ffffff",
      "--button-text": "#1f2933",
      "--button-border": "#94a3b8",
    },
    dark: {
      "--bg-color": "#0f172a",
      "--text-color": "#e2e8f0",
      "--link-color": "#93c5fd",
      "--table-head-bg": "#0b1220",
      "--table-even-row": "#1f2937",
      "--button-bg": "#1e293b",
      "--button-text": "#e2e8f0",
      "--button-border": "#64748b",
    },
  };

  if (!button) {
    return;
  }

  const applyTheme = (theme) => {
    const next = theme === darkValue ? darkValue : lightValue;
    document.documentElement.setAttribute("data-theme", next);
    document.body.setAttribute("data-theme", next);
    document.body.classList.toggle("theme-dark", next === darkValue);
    button.textContent = next === darkValue ? "Switch to light mode" : "Switch to dark mode";
    localStorage.setItem(storageKey, next);
    const vars = themeVars[next];
    Object.keys(vars).forEach((key) => {
      document.documentElement.style.setProperty(key, vars[key]);
    });
  };

  const saved = localStorage.getItem(storageKey);
  applyTheme(saved === darkValue ? darkValue : lightValue);

  button.addEventListener("click", () => {
    const current = document.documentElement.getAttribute("data-theme") || lightValue;
    applyTheme(current === darkValue ? lightValue : darkValue);
  });
})();
