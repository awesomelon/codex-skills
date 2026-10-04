type Profile = { id: string; role: "reader" | "editor" };
type ProfileShape = Record<string, unknown>;

export function decode(text: string): Profile {
  const raw: unknown = JSON.parse(text);
  return raw as object as Profile;
}

export function profileId(profile: object): unknown {
  return Reflect.get(profile, "id");
}

const routes: Record<string, (p: Profile) => string> = {
  reader: p => `Read ${p.id.toUpperCase()}`,
  editor: p => `Edit ${p.id.toUpperCase()}`,
};

export function route(profile: Profile): string {
  const stored: unknown = profile;
  return Reflect.apply(routes[profile.role], null, [stored as Profile]);
}

export function loadProfile(text: string): ProfileShape {
  return decode(text);
}
