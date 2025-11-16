import React, { useState } from 'react'
method: 'POST',
body: data,
})
if (!res.ok) throw new Error('Server error: ' + res.status)
const json = await res.json()
setCaption(json.caption)
setRaw(json.raw)
} catch (err) {
setError(err.message)
} finally {
setLoading(false)
}
}


return (
<div style={{maxWidth:700, margin:'2rem auto', fontFamily:'system-ui, Arial'}}>
<h1>Image Caption Generator</h1>
<form onSubmit={handleSubmit}>
<input
type="file"
accept="image/*"
onChange={(e) => setFile(e.target.files[0])}
/>
<div style={{marginTop:12}}>
<button type="submit" disabled={loading || !file}>
{loading ? 'Generating...' : 'Generate Caption'}
</button>
</div>
</form>


{error && <p style={{color:'red'}}>{error}</p>}


{caption && (
<div style={{marginTop:20, padding:12, border:'1px solid #ddd', borderRadius:8}}>
<h3>Caption</h3>
<p>{caption}</p>
<button onClick={() => navigator.clipboard?.writeText(caption)}>Copy</button>
<details style={{marginTop:8}}>
<summary>Raw output</summary>
<pre style={{whiteSpace:'pre-wrap'}}>{JSON.stringify(raw, null, 2)}</pre>
</details>
</div>
)}
</div>
)
}
