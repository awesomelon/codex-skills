# Component composition and shared state

Use these criteria when consumers need different component contents, actions, or state management. The [source record](sources.md) identifies the Vercel guidance and adaptations.

## Express meaningful differences

Reuse components and hooks where consumers need the same behavior. When flags such as `isEditing` and `isReply` create conflicting combinations or spread mode checks across unrelated parts, consider named variants composed from shared elements. A small `variant` prop can remain clearer when the differences are limited. Ordinary boolean state such as `disabled`, `checked`, and `isLoading` is not a design defect.

Let callers supply `children` or named React node props when they only need to place content. Keep render props when a component supplies data to the caller, such as `renderItem({ item, index })`. Do not add Context just to replace a useful callback.

For example, these JSX fragments share an input while making the available actions visible. The handlers retain their existing form submission behavior:

```tsx
// Reply composer
<form onSubmit={submitReply}>
  <MessageInput value={draft} onChange={setDraft} />
  <button type="submit" disabled={isSending}>Reply</button>
</form>

// Edit composer
<form onSubmit={saveEdit}>
  <MessageInput value={draft} onChange={setDraft} />
  <button type="button" onClick={cancelEdit}>Cancel</button>
  <button type="submit" disabled={isSaving}>Save</button>
</form>
```

Named components are useful when they clarify a real use case, not merely because two callers differ. Preserve existing public props unless the requested change requires an API change; explain any migration for existing callers.

## Choose how parts share state

Compound components are useful when callers need to rearrange or omit related parts that share behavior. Context can let those parts read shared values without passing the same props through many levels. Neither Context nor a dotted API such as `Composer.Input` is required for ordinary component reuse. Prefer explicit props when the small number of consumers remains easy to follow.

If a preview or submit button needs the same draft as the editor, move that draft to their nearest suitable common parent. Add a provider when the consumers benefit from Context; do not keep a second copy synchronized through an Effect or move rendered state into a ref. Components can share a provider without being visually inside the same box. Keep independent editor instances in separate state scopes and retain intentional reset behavior.

When the same UI actually needs local and externally managed state, keep the specific state hook in the parent or provider and pass the values and actions the UI needs. Grouping them as `state`, `actions`, and `meta` is an option, not a required schema. Prefer meaningful actions such as `changeText` or `submit` when exposing a generic setter would couple consumers to all stored fields. Keep existing request/cache behavior; a provider is not a reason to replace the data library.

For a required provider, handle its absence explicitly when reading a nullable Context instead of assuming a non-null value. Decide whether an optional provider has a meaningful fallback. Consider which consumers update on each keystroke: one Context containing state and actions also updates consumers that only read actions. If this causes a real cost, consider separate contexts or existing selective subscriptions; merely grouping fields does not reduce subscriptions. Use [performance.md](performance.md) for rendering evidence and optimization choices.

## Versions and behavior preservation

Use the target project's React APIs and types. React 18 uses `Context.Provider`, `useContext`, and `forwardRef` when forwarding a ref. React 19 supports the shorter provider syntax, `use(Context)`, and ref props on function components. `useContext` remains valid; do not classify it as incorrect or require an unrelated conversion. Consider ref props for React 19 code while preserving the supported React versions of shared libraries.

When changing composition, retain controlled input behavior, form submission, focus, labels, and keyboard interaction using the checks in [react-correctness.md](react-correctness.md). For a shared provider, also check that editing or resetting one instance leaves another unchanged. Choose checks for the actual change rather than requiring every composition technique.
