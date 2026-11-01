# Troubleshooting & FAQ

*Common questions and fixes for both apps.*

## Editing & selection

??? question "Clicking a point after zooming/panning selects the wrong spot"
    This was fixed — make sure you're on the latest version. Hit points are matched in the
    same coordinate space as the zoomed/panned view.

??? question "My handle or base won't attach"
    Open the **connection dialog** when adding the part and pick a valid connection
    (e.g. **Top+Bottom → Surface** for a handle). Parts need a compatible connection on
    both source and target.

## Stamps & reliefs

??? question "My stamp text is mirrored"
    Fixed in a recent build. Update to the latest version; text now reads correctly as it
    wraps around the body.

??? question "The relief/text isn't visible from some angles"
    Reliefs and text use a double-sided surface so they render from both sides. If a stamp
    looks missing, rotate the view — it may be on the far side of the body — or increase its
    scale with the corner handles.

??? question "How do I resize a stamp?"
    Select it in the **3D** view and drag a **corner handle** of its selection box — on
    Android with a touch drag, on macOS with a click drag (a plain drag on the body moves
    the stamp instead). You can also use the size slider in the stamp editor, or pinch on
    Android. See [Placing & scaling](../stamps/placing.md).

??? question "A recessed stamp doesn't print as a carved-in mark"
    A recessed stamp currently shows pressed into the surface on screen, but it isn't yet
    cut out of the wall in the exported STL, so it won't print as a true incised cavity.
    **Raised** stamps print correctly. This is a known limitation being worked on.

## Files

??? question "Where are my files saved?"
    Both apps use the system save/open dialogs and store projects as **JSON**. On Android the
    default suggested extension is `.json`. See [Save & open](../files/save-open.md).

??? question "My customized cross-section curve didn't save"
    Fixed — the cross-section is now serialized with the project. Re-save with the latest
    version and the custom curve persists.

## Export & printing

??? question "The export seems to hang"
    Larger models with molds take a moment — watch for the export spinner. Let it finish
    before switching views.

??? question "The printed piece is the wrong size"
    Check **scale** before exporting, and for molds account for clay **shrinkage**.
    See [Scale & bed fit](../exporting/scale.md).

## macOS specific

??? question "Closing the window quit the app / parts behave oddly"
    Fixed. Closing the last window keeps the app alive, and **New**, **Open**, or
    **New from Template** reopens a window automatically.

!!! tip "Still stuck?"
    Open an issue on the [project repository](https://github.com/dromidror/pottery-wheel-docs).
