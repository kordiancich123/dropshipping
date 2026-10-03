/* GALAKTIS: menu, koszyk wysuwany, galeria, warianty, sticky, animacje */
(function () {
  'use strict';
  var d = document;
  d.documentElement.classList.add('gx-js');
  var root = (window.Shopify && Shopify.routes && Shopify.routes.root) || '/';
  var FREE_SHIP = 20000; // grosze; próg darmowej dostawy

  function money(c) {
    return (c / 100).toFixed(2).replace('.', ',') + ' zł';
  }
  function $(s, c) { return (c || d).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); }

  /* menu mobilne */
  var mnav = $('#gx-mnav');
  function toggleNav(open) {
    if (!mnav) return;
    mnav.classList.toggle('is-open', open);
    mnav.setAttribute('aria-hidden', !open);
    var b = $('[data-gx-burger]');
    if (b) b.setAttribute('aria-expanded', open);
    d.body.style.overflow = open ? 'hidden' : '';
  }
  $$('[data-gx-burger]').forEach(function (b) { b.addEventListener('click', function () { toggleNav(true); }); });
  $$('[data-gx-mnav-close]').forEach(function (b) { b.addEventListener('click', function () { toggleNav(false); }); });
  if (mnav) mnav.addEventListener('click', function (e) { if (e.target === mnav || e.target.tagName === 'A') toggleNav(false); });

  /* koszyk */
  var drawer = $('#gx-drawer');
  function openDrawer(open) {
    if (!drawer) return;
    drawer.classList.toggle('is-open', open);
    drawer.setAttribute('aria-hidden', !open);
    d.body.style.overflow = open ? 'hidden' : '';
    if (open) { var c = $('[data-gx-drawer-close]', drawer); if (c) c.focus(); }
  }
  function renderCart(cart) {
    $$('[data-gx-count]').forEach(function (el) { el.textContent = cart.item_count; el.setAttribute('data-count', cart.item_count); });
    if (!drawer) return;
    var lines = $('[data-gx-lines]', drawer);
    var foot = $('[data-gx-foot]', drawer);
    if (!cart.items.length) {
      lines.innerHTML = '<p class="gx-empty">Twój koszyk jest pusty.</p>';
      foot.hidden = true;
    } else {
      lines.innerHTML = cart.items.map(function (it) {
        var img = it.image ? it.image + (it.image.indexOf('?') > -1 ? '&' : '?') + 'width=160' : '';
        return '<div class="gx-line">' +
          (img ? '<img src="' + img + '" alt="" width="72" height="72" loading="lazy">' : '<span></span>') +
          '<div><b>' + it.product_title + '</b><small>' + (it.variant_title || '') + '</small>' +
          '<div class="gx-qty"><button type="button" data-gx-qty="' + it.key + '" data-q="' + (it.quantity - 1) + '" aria-label="Zmniejsz ilość">−</button>' +
          '<span>' + it.quantity + '</span>' +
          '<button type="button" data-gx-qty="' + it.key + '" data-q="' + (it.quantity + 1) + '" aria-label="Zwiększ ilość">+</button></div></div>' +
          '<span class="gx-line__pr">' + money(it.final_line_price) + '</span></div>';
      }).join('');
      foot.hidden = false;
      $('[data-gx-subtotal]', drawer).textContent = money(cart.total_price);
    }
    var left = FREE_SHIP - cart.total_price;
    var ship = $('[data-gx-ship]', drawer);
    if (ship) {
      $('[data-gx-ship-txt]', ship).textContent = left > 0
        ? 'Brakuje ' + money(left) + ' do darmowej dostawy'
        : 'Masz darmową dostawę';
      $('i', ship).style.width = Math.min(100, cart.total_price / FREE_SHIP * 100) + '%';
    }
  }
  function getCart() { return fetch(root + 'cart.js').then(function (r) { return r.json(); }).then(renderCart); }
  function addToCart(id, qty, btn) {
    if (btn) btn.disabled = true;
    return fetch(root + 'cart/add.js', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({ items: [{ id: Number(id), quantity: qty || 1 }] })
    }).then(function (r) { if (!r.ok) throw r; return getCart(); })
      .then(function () { openDrawer(true); })
      .catch(function () { window.location.href = root + 'cart'; })
      .finally(function () { if (btn) btn.disabled = false; });
  }
  function changeLine(key, q) {
    return fetch(root + 'cart/change.js', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({ id: key, quantity: Math.max(0, q) })
    }).then(function (r) { return r.json(); }).then(renderCart);
  }
  if (drawer) {
    drawer.addEventListener('click', function (e) {
      var q = e.target.closest('[data-gx-qty]');
      if (q) changeLine(q.getAttribute('data-gx-qty'), Number(q.getAttribute('data-q')));
      if (e.target.closest('[data-gx-drawer-close]') || e.target.classList.contains('gx-drawer__bg')) openDrawer(false);
    });
  }
  $$('[data-gx-cart-open]').forEach(function (a) {
    a.addEventListener('click', function (e) { if (drawer) { e.preventDefault(); getCart(); openDrawer(true); } });
  });
  d.addEventListener('keydown', function (e) { if (e.key === 'Escape') { openDrawer(false); toggleNav(false); } });

  /* formularze dodawania do koszyka */
  $$('form[data-gx-add]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var id = (f.querySelector('input[name="id"]:checked') || f.querySelector('[name="id"]')).value;
      addToCart(id, 1, f.querySelector('[type="submit"]'));
    });
  });
  $$('[data-gx-add-variant]').forEach(function (b) {
    b.addEventListener('click', function () { addToCart(b.getAttribute('data-gx-add-variant'), 1, b); });
  });

  /* warianty: cena, sticky */
  $$('[data-gx-product]').forEach(function (p) {
    var now = $('[data-gx-price]', p), was = $('[data-gx-was]', p), save = $('[data-gx-save]', p);
    p.addEventListener('change', function (e) {
      if (e.target.name !== 'id') return;
      var o = e.target.dataset;
      now.textContent = o.price;
      if (was) { was.textContent = o.was || ''; was.hidden = !o.was; }
      if (save) { save.textContent = o.save || ''; save.hidden = !o.save; }
      $$('[data-gx-sticky-price]').forEach(function (s) { s.textContent = o.price; });
    });
  });
  var stickyBtn = $('[data-gx-sticky-add]');
  if (stickyBtn) {
    stickyBtn.addEventListener('click', function () {
      var c = d.querySelector('[data-gx-product] input[name="id"]:checked');
      if (c) addToCart(c.value, 1, stickyBtn);
    });
  }

  /* sticky: widoczny, gdy nie widać ani hero CTA, ani przycisku produktu */
  var sticky = $('#gx-sticky');
  var watch = $$('[data-gx-watch]');
  if (sticky && watch.length && 'IntersectionObserver' in window) {
    var vis = new Map();
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { vis.set(en.target, en.isIntersecting); });
      var any = false; vis.forEach(function (v) { if (v) any = true; });
      var on = !any;
      sticky.classList.toggle('is-on', on);
      sticky.setAttribute('aria-hidden', !on);
    });
    watch.forEach(function (w) { io.observe(w); });
  }

  /* galeria + powiększenie */
  $$('[data-gx-gallery]').forEach(function (g) {
    var main = $('[data-gx-main] img', g), dlg = $('dialog', g), big = dlg && $('img', dlg);
    $$('[data-gx-thumb]', g).forEach(function (t) {
      t.addEventListener('click', function () {
        $$('[data-gx-thumb]', g).forEach(function (x) { x.setAttribute('aria-current', 'false'); });
        t.setAttribute('aria-current', 'true');
        main.src = t.dataset.src; main.srcset = t.dataset.srcset || ''; main.alt = t.dataset.alt || '';
        if (big) big.src = t.dataset.full;
      });
    });
    var m = $('[data-gx-main]', g);
    if (m && dlg && dlg.showModal) m.addEventListener('click', function () { dlg.showModal(); });
  });

  /* wideo w hero: ładowane po załadowaniu strony, żeby nie spowalniać pierwszego wyświetlenia */
  window.addEventListener('load', function () {
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var save = navigator.connection && navigator.connection.saveData;
    if (reduce || save) return;
    $$('[data-gx-lazy-video]').forEach(function (v) {
      v.src = v.getAttribute('data-gx-lazy-video');
      v.addEventListener('playing', function () { v.classList.add('is-on'); }, { once: true });
      var p = v.play(); if (p && p.catch) p.catch(function () {});
    });
  });

  /* animacje przy przewijaniu */
  if ('IntersectionObserver' in window) {
    var rio = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-in'); rio.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    $$('.gx-reveal').forEach(function (el) { rio.observe(el); });
  } else {
    $$('.gx-reveal').forEach(function (el) { el.classList.add('is-in'); });
  }
})();
