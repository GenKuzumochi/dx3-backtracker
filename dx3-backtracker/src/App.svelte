<script lang="ts">
  import Bar from "./lib/Bar.svelte";
  let dice = parseInt(
    new URLSearchParams(location.hash.substring(1)).get("dice") ?? "0",
  );
  let fix = parseInt(
    new URLSearchParams(location.hash.substring(1)).get("fix") ?? "0",
  );
  let start = parseInt(
    new URLSearchParams(location.hash.substring(1)).get("start") ?? "100",
  );

  $: {
    const p = new URLSearchParams(location.hash.substring(1));
    p.set("dice", (dice ?? 0).toString());
    p.set("fix", (fix?? 0).toString());
    p.set("start", (start??0).toString());
    location.hash = p.toString();
  }
</script>

<header>
  <h1>ダブルクロス バックトラック計算機</h1>
  <a href="./help.jpg" class="help">Help</a>
  表の起点<input bind:value={start} type="number" min="0" />
  修正値(Eロイス、メモリーなど):
  <input bind:value={dice} type="number" min="0" />D10+
  <input bind:value={fix} type="number" min="0" />
  <br/>

  減少期待値 <b>{dice * 5.5 + fix}</b>
</header>
<main>
  <div class="flex sticky th">
    <div class="encroachment encroachment-th">
      <div style="writing-mode:vertical-lr; flex-grow:1;">残ロイス</div>
      <div style="border-top: 1px solid #CCC;">侵蝕</div>
    </div>
    <div class="loise-count">
      <div class="loise-a">1</div>
      <div class="loise-b">
        {dice + 1}/{dice + 1 * 2}/{dice + 1 * 3} <span>個</span>
      </div>
    </div>
    <div class="loise-count">
      <div class="loise-a">2</div>
      <div class="loise-b">
        {dice + 2}/{dice + 2 * 2}/{dice + 2 * 3} <span>個</span>
      </div>
    </div>
    <div class="loise-count">
      <div class="loise-a">3</div>
      <div class="loise-b">
        {dice + 3}/{dice + 3 * 2}/{dice + 3 * 3} <span>個</span>
      </div>
    </div>
    <div class="loise-count">
      <div class="loise-a">4</div>
      <div class="loise-b">
        {dice + 4}/{dice + 4 * 2}/{dice + 4 * 3} <span>個</span>
      </div>
    </div>
    <div class="loise-count">
      <div class="loise-a">5</div>
      <div class="loise-b">
        {dice + 5}/{dice + 5 * 2}/{dice + 5 * 3} <span>個</span>
      </div>
    </div>
    <div class="loise-count">
      <div class="loise-a">6</div>
      <div class="loise-b">
        {dice + 6}/{dice + 6 * 2}/{dice + 6 * 3} <span>個</span>
      </div>
    </div>
    <div class="loise-count">
      <div class="loise-a">7</div>
      <div class="loise-b">
        {dice + 7}/{dice + 7 * 2}/{dice + 7 * 3} <span>個</span>
      </div>
    </div>
  </div>
  {#each Array(20) as _, i}
    <div class="flex">
      <div class="encroachment">{start + i * 5}</div>
      <Bar encroachment={start + i * 5} loise={1} {dice} {fix} />
      <Bar encroachment={start + i * 5} loise={2} {dice} {fix} />
      <Bar encroachment={start + i * 5} loise={3} {dice} {fix} />
      <Bar encroachment={start + i * 5} loise={4} {dice} {fix} />
      <Bar encroachment={start + i * 5} loise={5} {dice} {fix} />
      <Bar encroachment={start + i * 5} loise={6} {dice} {fix} />
      <Bar encroachment={start + i * 5} loise={7} {dice} {fix} />
    </div>
  {/each}
</main>

<style>
  :root {
    --seven: calc(100vw / 7 - 10px);
  }
  h1 {
    font-size: 1.5rem;
  }
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
  main {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .flex {
    display: flex;
    gap: 4px;
    align-items: center;
  }
  header {
    margin: 1rem;
  }
  .encroachment {
    width: 30px;
    font-weight: bold;
    align-self: stretch;
    align-items: center;
    display: flex;
    border-bottom: 1px solid #ccc;
    border-top: 1px solid #ccc;
  }
  .loise-count {
    width: var(--seven);
    display: flex;
    align-items: center;
    justify-items: center;
  }
  .loise-a {
    grid-area: a;
    font-size: 2rem;
    padding: 0 1rem;
  }
  .loise-b {
    grid-area: b;
    font-size: 0.8rem;
  }
  .sticky {
    position: sticky;
    top: 0;
    background: #fff;
  }
  header input {
    width: 50px;
  }
  .encroachment-th {
    font-size: 10px;
    
    font-weight: normal;
    display: flex;
    flex-direction: column;
    align-items: end;
    align-self: normal;
    background: white;
  }

  .th {
  }
  .th>div {
    background: white;
  }

  .help {
    position: absolute;
    top:0;
    left: 0;
    background:white;
    }
  @media screen and (max-width: 600px) {
    :root {
      --seven: calc(100vw / 7 - 7px);
    }
    .encroachment {
      font-size: 12px;
      width: 20px;
    }
    
    .encroachment-th {
      font-size: 10px;
    }
    .loise-count {
      flex-direction: column;
    }
    .loise-b {
      display: none;
    }
  }
</style>
