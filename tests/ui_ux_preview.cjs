// Optional browser regression for the bundled low-fidelity comparison, using an existing Playwright install.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { pathToFileURL } = require('node:url');

async function main() {
  const playwright = require(process.argv[2] || 'playwright-core');
  const executablePath = process.argv[3];
  const output = fs.mkdtempSync(path.join(os.tmpdir(), 'ui-ux-preview-'));
  const browser = await playwright.chromium.launch({ headless: true, ...(executablePath ? { executablePath } : {}) });
  const page = await browser.newPage();
  const errors = [];
  const requests = [];
  page.on('pageerror', (error) => errors.push(error.message));
  await page.route(/^https?:/, (route) => { requests.push(route.request().url()); return route.abort(); });
  try {
    const source = path.resolve(__dirname, '../packs/developer-skills/skills/ultimate-ui-ux/assets/comparison.html');
    await page.goto(pathToFileURL(source).href);
    const products = page.getByRole('tab', { name: 'Products', exact: true });
    const channel = page.getByRole('tab', { name: 'Channel', exact: true });
    const reviews = page.getByRole('tab', { name: 'Reviews', exact: true });
    const expectSelected = async (id) => {
      const state = await page.locator('[role="tab"]').evaluateAll((tabs) => tabs.map((tab) => ({
        id: tab.id,
        selected: tab.getAttribute('aria-selected') === 'true',
        visible: !document.getElementById(tab.getAttribute('aria-controls')).hidden,
      })));
      assert.deepEqual(state.filter((tab) => tab.selected).map((tab) => tab.id), [id]);
      assert.deepEqual(state.filter((tab) => tab.visible).map((tab) => tab.id), [id]);
    };
    await expectSelected('tab-products');
    await channel.click();
    await expectSelected('tab-channel');
    await reviews.click();
    await expectSelected('tab-reviews');
    await products.click();
    await products.press('ArrowRight');
    assert.equal(await channel.evaluate((element) => element === document.activeElement), true);
    await expectSelected('tab-products');
    await channel.press('Tab');
    assert.equal(await page.locator('#panel-products').evaluate((element) => element === document.activeElement), true);
    await page.keyboard.press('Shift+Tab');
    assert.equal(await products.evaluate((element) => element === document.activeElement), true);
    await products.press('ArrowRight');
    await channel.press('Enter');
    await expectSelected('tab-channel');
    await channel.press('End');
    assert.equal(await reviews.evaluate((element) => element === document.activeElement), true);
    await expectSelected('tab-channel');
    await reviews.press('Space');
    await expectSelected('tab-reviews');
    await reviews.press('Home');
    assert.equal(await products.evaluate((element) => element === document.activeElement), true);
    await products.press('ArrowLeft');
    assert.equal(await reviews.evaluate((element) => element === document.activeElement), true);
    await reviews.press('ArrowRight');
    await products.press('Enter');
    await products.press('Tab');
    assert.equal(await page.locator('#panel-products').evaluate((element) => element === document.activeElement), true);
    for (const width of [1280, 390, 320]) {
      await page.setViewportSize({ width, height: 900 });
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true, `overflow at ${width}px`);
      for (const tab of [products, channel, reviews]) {
        await tab.click();
        const id = await tab.getAttribute('id');
        await expectSelected(id);
        assert.equal(await page.locator('[role="tab"][tabindex="0"]').count(), 1);
        const bounds = await tab.boundingBox();
        assert.ok(bounds.x >= 0 && bounds.x + bounds.width <= width, `tab outside ${width}px viewport`);
      }
      await products.click();
      await page.screenshot({ path: path.join(output, `comparison-${width}.png`), fullPage: true });
    }
    assert.deepEqual(errors, []);
    assert.deepEqual(requests, []);
    console.log('PASS: panel switching, manual keyboard activation, focus, wraparound, no overflow at 1280/390/320px, no network writes or script errors.');
    console.log(`Screenshots: ${output}`);
  } finally {
    await browser.close();
  }
}

main().catch((error) => { console.error(error); process.exitCode = 1; });
