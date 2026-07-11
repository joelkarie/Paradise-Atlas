export async function imageExists(url) {
    const response = await fetch(url, { method: "HEAD" });
    return response.ok;
}