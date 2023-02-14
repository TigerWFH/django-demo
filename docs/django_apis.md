# Django Apis

## path(route, view, kwargs, name)

- `route:`包含 URL Pattern 的字符串，只匹配 path，不匹配 domain 和 params
- `view:`会被注入一个 HttpRequest 参数，渲染 template 或者直接返回一个 HttpResponse
- `kwagrs：`注入 view 的额外参数
- `name：`命名路由
