// Theme toggle (dark by default, saved in the browser)
const root = document.documentElement;
document.getElementById("theme-toggle").addEventListener("click", () => {
    const next = root.dataset.theme === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    localStorage.setItem("theme", next);
});

// Mobile menu toggle
const menuBtn = document.getElementById("menu-toggle");
const nav = document.getElementById("nav");
menuBtn.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    menuBtn.setAttribute("aria-expanded", open);
});

// Typing effect for the hero role
const typed = document.getElementById("typed");
if (typed && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    const roles = JSON.parse(typed.dataset.roles);
    let r = 0, c = 0, deleting = false;
    (function tick() {
        const word = roles[r];
        typed.textContent = word.slice(0, c);
        if (!deleting && c === word.length) { deleting = true; return setTimeout(tick, 1400); }
        if (deleting && c === 0) { deleting = false; r = (r + 1) % roles.length; }
        c += deleting ? -1 : 1;
        setTimeout(tick, deleting ? 40 : 90);
    })();
}

// Skills filter tabs
document.querySelectorAll(".tab").forEach(tab => {
    tab.addEventListener("click", () => {
        document.querySelectorAll(".tab").forEach(t => {
            t.classList.toggle("active", t === tab);
            t.setAttribute("aria-selected", t === tab);
        });
        const f = tab.dataset.filter;
        document.querySelectorAll(".chip").forEach(chip => {
            chip.hidden = f !== "all" && chip.dataset.cat !== f;
        });
    });
});

// Project card details toggle
document.querySelectorAll(".card .toggle").forEach(btn => {
    btn.addEventListener("click", () => {
        const more = btn.parentElement.querySelector(".more");
        const open = more.hidden;
        more.hidden = !open;
        btn.setAttribute("aria-expanded", open);
        btn.textContent = open ? "Hide details" : "Show details";
    });
});

// Contact form -> Formspree (no page reload)
const form = document.getElementById("contact-form");
if (form) {
    const status = document.getElementById("form-status");
    form.addEventListener("submit", async e => {
        e.preventDefault();
        status.className = "";
        status.textContent = "Sending...";
        try {
            const res = await fetch(form.action, {
                method: "POST",
                body: new FormData(form),
                headers: { Accept: "application/json" }
            });
            if (!res.ok) throw new Error();
            form.reset();
            status.className = "ok";
            status.textContent = "Message sent. Thank you, I'll reply soon.";
        } catch {
            status.className = "err";
            status.textContent = "Message not sent. Check your connection and try again.";
        }
    });
}

// Project carousels
document.querySelectorAll(".carousel").forEach(car => {
    const track = car.querySelector(".carousel-track");
    const step = () => {
        const slide = track.querySelector(".slide");
        const gap = parseFloat(getComputedStyle(track).columnGap) || 0;
        return slide.getBoundingClientRect().width + gap;
    };
    car.querySelector(".car-prev").addEventListener("click", () => track.scrollBy({ left: -step() }));
    car.querySelector(".car-next").addEventListener("click", () => track.scrollBy({ left: step() }));
});
