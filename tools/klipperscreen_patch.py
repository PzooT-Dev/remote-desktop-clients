from pathlib import Path

path = Path("bVNC/src/main/java/com/iiordanov/bVNC/RemoteCanvasActivity.java")
text = path.read_text(encoding="utf-8")

old = '''    public void showActionBar() {
        handler.removeCallbacks(actionBarShower);
        handler.postAtTime(actionBarShower, SystemClock.uptimeMillis() + 50);
        handler.removeCallbacks(actionBarHider);
        handler.postAtTime(actionBarHider, SystemClock.uptimeMillis() + hideToolbarDelay);
    }
'''

new = '''    public void showActionBar() {
        // KlipperScreen viewer: keep the in-session bVNC control bar permanently hidden.
        // Connection setup and settings remain available outside RemoteCanvasActivity.
        handler.removeCallbacks(actionBarShower);
        handler.removeCallbacks(actionBarHider);
        if (toolbar != null) {
            toolbar.setVisibility(View.GONE);
        }
        ActionBar actionBar = getSupportActionBar();
        if (actionBar != null) {
            actionBar.hide();
        }
    }
'''

if old not in text:
    raise SystemExit("Expected showActionBar() block not found; upstream changed")

text = text.replace(old, new, 1)
path.write_text(text, encoding="utf-8")
print("Applied KlipperScreen toolbar suppression patch")
