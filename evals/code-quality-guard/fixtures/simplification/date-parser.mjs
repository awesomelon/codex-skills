function createParser({ mode }) {
  if (mode !== "iso-date") {
    throw new RangeError("Unsupported parser mode");
  }
  const steps = [
    (value) => {
      if (typeof value !== "string") {
        throw new TypeError("Expected a date string");
      }
      return value;
    },
    (value) => {
      if (!/^\d{4}-\d{2}-\d{2}$/.test(value) || value.slice(0, 4) < "1000") {
        throw new RangeError("Expected YYYY-MM-DD in years 1000-9999");
      }
      return value;
    },
    (value) => {
      const date = new Date(`${value}T00:00:00.000Z`);
      if (!Number.isFinite(date.getTime()) || date.toISOString().slice(0, 10) !== value) {
        throw new RangeError("Invalid calendar date");
      }
      return value;
    },
  ];
  return (value) => steps.reduce((current, step) => step(current), value);
}

export const parseCalendarDate = createParser({ mode: "iso-date" });
