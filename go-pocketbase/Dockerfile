FROM --platform=$BUILDPLATFORM golang:1.22 as builder
ARG TARGETOS
ARG TARGETARCH

WORKDIR /workspace
COPY go.mod go.sum ./
RUN go mod download

COPY migrations/ migrations/
COPY main.go .

RUN CGO_ENABLED=1 GOOS=${TARGETOS:-linux} GOARCH=${TARGETARCH} go build -o server main.go

FROM gcr.io/distroless/base-debian12:latest
WORKDIR /
COPY --from=builder /workspace/server .
EXPOSE 8040
ENTRYPOINT ["/server", "serve", "--http=0.0.0.0:8040"]
