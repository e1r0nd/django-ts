const protocol: string = window.location.protocol;
const hostname: string = window.location.hostname;
const port: string = window.location.port ? `:${window.location.port}` : "";

/** Specify the endpoint for DEV and PRD */
export const ENDPOINT: string = `${protocol}//${hostname}${port}/api/`;
